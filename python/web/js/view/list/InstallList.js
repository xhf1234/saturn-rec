/*jslint browser: true, devel: true, indent: 4, nomen:true, vars: true */
/*global define */

define(function (require, exports, module) {
    "use strict";

    var BaseList = require('./BaseList');

    var InstallItem = require('./item/InstallItem');

    var InstallList = BaseList.extend({
        className: BaseList.prototype.className + ' well',

        headerList: ['已安装应用'],
        
        render: function (recommends) {
            BaseList.prototype.render.apply(this, arguments);

            recommends.forEach(function (app) {
                this.appendItem(InstallItem, app);
            }, this);
        }
    });

    return InstallList;
});

