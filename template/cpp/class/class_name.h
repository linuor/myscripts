/**
 * Copyright © 2016 {{info.author}}. All Rights Reserved.
 * @file {{info.dest | lower}}.cpp
 * @brief class file for {{info.dest}}
 * @author {{info.author}}
 * @version {{info.ver}}
 * @date {{info.date}}
 */

#ifndef {{info.dest | upper}}_H
#define {{info.dest | upper}}_H

namespace {{info.ns}} {

class {{info.dest}} {
public:
    {{info.dest}}(int argc, char **argv)
        : argc_(argc), argv_(argv), prop_(nullptr){};

    virtual ~{{info.dest}}() {
        delete prop_;
        prop_ = nullptr;
    };

protected:
    int argc_;
    char **argv_;
    int *prop_;
};

}  // namespace {{info.ns}}
#endif /* ifndef {{info.dest | upper}}_H */
