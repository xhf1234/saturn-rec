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

        Collection: null,

        Item: null,

        initialize: function () {
            var Collection = this.Collection;
            this.collection = new Collection();
        },

        render: function (renderData) {

            renderData = renderData || {};
            renderData = _.extend({
                headerList: this.headerList
            }, renderData);
            this.el.innerHTML = this.template(renderData);

            var datas = this.collection.toJSON();
            datas.forEach(function (data) {
                this.appendItem(this.Item, data);
            }, this);
        },

        appendItem: function (Item, data) {
            var item = new Item();
            item.render(data);
            this.$('tbody').append(item.el);
        },

        fetch: function (options) {
            options = options || {};
            options.success = this.onFetchedSuccess.bind(this);
            this.collection.fetch(options);
        },

        
        /* -------------------- Event Listener ----------------------- */
        
        onFetchedSuccess: function (evt) {
            this.render();
        }
    });

    return BaseList;
});
