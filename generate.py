#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
# Copyright © 2016 linuor. All Rights Reserved.
# @file generate.py
# @brief generate a set of files from jinja2 template
# @author linuor
# @version 0.1
# @date 2016-02-05

import os, sys
import argparse
import time
import codecs
from jinja2 import Environment, FileSystemLoader

class Generate(object):

    """Generate files from jinja2 template. """

    def __init__(self):
        """Init"""
        self.args    = None
        self.tmpldir = None
        self.srcdir  = None
        self.desdir  = None
        self.render  = None
        self.parser  = self.initParser()

    def initParser(self):
        """Init a argparse
        :returns: instance of a argparse
        """
        parser = argparse.ArgumentParser(description="Generate files from jinja template.")
        parser.add_argument(
                'dest',
                help    = 'Specify the location directory, also the name of the destination.',
                metavar = 'Destination',
        )
        parser.add_argument(
                '-t',
                '--template',
                help    = 'Specify the source template used for generation, also the name of the sub-directory under the template directory.',
                metavar = 'Template',
                dest    = 'tmpl',
                default = 'cpp'
        )
        parser.add_argument(
                '-a',
                '--author',
                help    = 'Specify the author name.',
                metavar = 'Author',
                dest    = 'author',
                default = os.getenv('USER', '')
        )
        parser.add_argument(
                '-d',
                '--date',
                help    = 'Specify the date.',
                metavar = 'Date',
                dest    = 'date',
                default = time.strftime("%Y-%m-%d %H:%M:%S")
        )
        parser.add_argument(
                '-v',
                '--version',
                help    = 'Specify the version.',
                metavar = 'Version',
                dest    = 'ver',
                default = '0.1'
        )
        return parser

    def getTmplDir(self):
        """Get the directory of the template files
        :returns: string of the directory
        """
        if self.tmpldir == None:
            self.tmpldir = sys.path[0]
            if os.path.isfile(self.tmpldir):
                self.tmpldir = os.path.dirname(self.tmpldir)
        return self.tmpldir

    def getSrcDir(self):
        """Get the source template files directory
        :returns: string of the directory
        """
        if self.srcdir == None:
            tmpl = self.getTmplDir()
            self.srcdir = os.path.join(tmpl, 'template', self.args.tmpl)
        return self.srcdir

    def getDesDir(self):
        """Get the destination directory
        :returns: string of the directory
        """
        if self.desdir == None:
            cwd = os.getcwd()
            self.desdir = os.path.join(cwd, self.args.dest)
        return self.desdir

    def printInfo(self):
        """Print all the information about the destination to be generated.
        """
        print("Generating %s with the following info:" % self.args.dest)
        print("From: %s" % self.srcdir)
        print("To: %s" % self.desdir)
        print("Template: %s" % self.args.tmpl)
        print("Author: %s" % self.args.author)
        print("Version: %s" % self.args.ver)
        print("Date: %s" % self.args.date)
        print("\n")

    def initJinja(self):
        self.render = Environment(loader = FileSystemLoader(self.getSrcDir()))


def main():
    gen = Generate()
    gen.args = gen.parser.parse_args()
    destDir = gen.getDesDir()
    rootDir = gen.getSrcDir()
    gen.initJinja()
    gen.printInfo()
    lrootDir = len(rootDir)
    for dirName, subdirList, fileList in os.walk(rootDir):
        dDir = destDir + dirName[lrootDir:]
        print("Creating directory %s ... " % dDir)
        if os.path.exists(dDir):
            print("Failed! Directory %s already exists." % dDir)
            return
        os.mkdir(dDir)
        for fname in fileList:
            fs = os.path.join(dirName, fname)
            fs = os.path.relpath(fs, gen.getSrcDir())
            fd = os.path.join(dDir, fname)
            print("\tGenerating %s" % fd)
            template = gen.render.get_template(fs)
            with codecs.open(fd, 'w', 'utf-8') as f:
                f.write(template.render(info=gen.args))

if __name__ == "__main__":
    main()
