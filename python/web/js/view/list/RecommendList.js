/*jslint browser: true, devel: true, indent: 4, nomen:true, vars: true */
/*global define */

define(function (require, exports, module) {
    "use strict";

    var BaseList = require('./BaseList');

    var RecommendItem = require('./item/RecommendItem');

    var RecommendList = BaseList.extend({
        className: BaseList.prototype.className + ' well',

        headerList: ['推荐应用', '评分'],
        
        render: function (recommends) {
            BaseList.prototype.render.apply(this, arguments);

            recommends.forEach(function (recApp) {
                this.appendItem(RecommendItem, recApp);
            }, this);
        }
    });

    return RecommendList;
});

