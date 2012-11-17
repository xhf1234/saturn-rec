/*jslint browser: true, devel: true, indent: 4, nomen:true, vars: true */
/*global define */

define(function (require, exports, module) {
    "use strict";

    var BaseCollection = require('./BaseCollection');
    var Install = require('../model/Install');

    var InstallCollection = BaseCollection.extend({
        model: Install,
        
        url: function () {
            return '/api/install/' + this.imei;
        },

        fetch: function (options) {
            this.imei = options.imei;
            BaseCollection.prototype.fetch.apply(this, arguments);
        }
    });

    return InstallCollection;
});

