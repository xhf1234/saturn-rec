/*jslint browser: true, devel: true, indent: 4, nomen:true, vars: true */
/*global define */

define(function (require, exports, module) {
    "use strict";

    var BaseList = require('./BaseList');

    var RecommendList = BaseList.extend({
        className: BaseList.prototype.className + ' well',

        headerList: ['推荐应用', '评分'],

        Collection: require('../../collection/RecommendCollection'),

        Item: require('./item/RecommendItem')
    });

    return RecommendList;
});

