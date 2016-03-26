#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016 linuor. All Rights Reserved.
# @file render.py
# @brief render a set of files from jinja2 template. Template never includes
# sub-directory. And it will replace the file name with the one given by user.
# @author linuor
# @version 0.1
# @date 2016-02-05

import os, sys
import argparse
import time
import codecs
from jinja2 import Environment, FileSystemLoader

class Render(object):

    """Render files from jinja2 template. """

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
        parser = argparse.ArgumentParser(description="Render files from jinja template.")
        parser.add_argument(
                'dest',
                help    = 'Specify the location directory, also the name of the destination.',
                metavar = 'Destination',
        )
        parser.add_argument(
                '-t',
                '--template',
                help    = 'Specify the source template used to render, also the name of the sub-directory under the template directory.',
                metavar = 'Template',
                dest    = 'tmpl',
                default = 'cpp/class'
        )
        parser.add_argument(
                '-n',
                '--namespace',
                help    = 'Specify the namespace for files to render.',
                metavar = 'Namespace',
                dest    = 'ns',
                default = 'name_space'
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
            (h,t) = os.path.split(self.args.dest)
            self.desdir = os.path.join(cwd, h)
            self.args.dest = t
        return self.desdir

    def printInfo(self):
        """Print all the information about the destination to be rendered.
        """
        print("Rendering %s with the following info:" % self.args.dest)
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
    render = Render()
    render.args = render.parser.parse_args()
    destDir = render.getDesDir()
    rootDir = render.getSrcDir()
    render.initJinja()
    render.printInfo()
    if not os.path.exists(destDir):
        t = raw_input("%s does not exist, create it or not? [y/n] " % destDir)
        if t.lower() in ['y', 'yes']:
            print("Creating directory %s ... " % destDir)
            os.makedirs(destDir)
        else:
            print("Abort!\n")
            return
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            fs = os.path.join(dirName, fname)
            fs = os.path.relpath(fs, rootDir)
            (h,t) = os.path.splitext(fname)
            fd = os.path.join(destDir, render.args.dest + t)
            if os.path.exists(fd):
                t = raw_input("\t%s exists, replace, skip or abort? [r/s/a] " % fd)
                t = t.lower()
                if t in ['a', 'abort']:
                    return
                if t in ['r', 'replace']:
                    pass
                else:
                    continue
            print("\tRendering %s" % fd)
            template = render.render.get_template(fs)
            with codecs.open(fd, 'w', 'utf-8') as f:
                f.write(template.render(info=render.args))

if __name__ == "__main__":
    main()
