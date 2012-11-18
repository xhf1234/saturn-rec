/*jslint browser: true, devel: true, indent: 4, nomen:true, vars: true */
/*global define */

define(function (require, exports, module) {
    "use strict";

    var BaseList = require('./BaseList');

    var InstallList = BaseList.extend({
        className: BaseList.prototype.className + ' well',

        headerList: ['已安装应用'],

        Collection: require('../../collection/InstallCollection'),

        Item: require('./item/InstallItem')
    });

    return InstallList;
});

