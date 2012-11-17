/*jslint browser: true, devel: true, indent: 4, nomen:true, vars: true */
/*global define */

define(function (require, exports, module) {
    "use strict";

    var BaseItem = require('./BaseItem');

    var InstallItem = BaseItem.extend({
        tmpl: require('/list/item/InstallItem.handlebars'),

        render: function (recApp) {
            this.el.innerHTML = this.template(recApp);
        }
    });

    return InstallItem;
});

