/*jslint browser: true, devel: true, indent: 4, nomen:true, vars: true */
/*global define */

define(function (require, exports, module) {
    "use strict";

    var BaseItem = require('./BaseItem');

    var RecommendItem = BaseItem.extend({
        tmpl: require('/list/item/RecommendItem.handlebars'),

        render: function (recApp) {
            this.el.innerHTML = this.template(recApp);
        }
    });

    return RecommendItem;
});

