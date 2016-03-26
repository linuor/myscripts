/**
 * Copyright © 2016 {{info.author}}. All Rights Reserved.
 * @file main.cpp
 * @brief main file for {{info.dest}}
 * @author {{info.author}}
 * @version {{info.ver}}
 * @date {{info.date}}
 */

#include <iostream>
#include <unistd.h>

int main(int argc, char *argv[])
{
    std::cout << "Run process." << std::endl;
    pid_t pid = fork();
    if (pid == 0) {
        std::cout << "Here is the child process." << std::endl;
    }
    else if (pid == -1) {
        std::cout << "Fork failed." << std::endl;
    }
    else {
        std::cout << "Here is remain in parent process." << std::endl;
        std::cin >> pid;
    }
    return 0;
}
