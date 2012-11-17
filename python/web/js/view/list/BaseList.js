/*jslint browser: true, devel: true, indent: 4, nomen:true, vars: true */
/*global define */

define(function (require, exports, module) {
    "use strict";

    var BaseView = require('../BaseView');
    var _ = require('../../lib/underscore');

    var BaseList = BaseView.extend({
        tagName: 'table',

        className: 'table',

        headerList: [],

        tmpl: require('/list/BaseList.handlebars'),

        render: function (renderData) {
            renderData = renderData || {};

            renderData = _.extend({
                headerList: this.headerList
            }, renderData);
            this.el.innerHTML = this.template(renderData);
        },

        appendItem: function (Item, data) {
            var item = new Item();
            item.render(data);
            this.$('tbody').append(item.el);
        }
    });

    return BaseList;
});
