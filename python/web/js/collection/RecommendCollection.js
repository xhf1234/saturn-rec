/*jslint browser: true, devel: true, indent: 4, nomen:true, vars: true */
/*global define */

define(function (require, exports, module) {
    "use strict";

    var BaseCollection = require('./BaseCollection');
    var Recommend = require('../model/Recommend');

    var RecommendCollection = BaseCollection.extend({
        model: Recommend,
        
        url: function () {
            return '/api/recommends/' + this.imei;
        },

        fetch: function (options) {
            this.imei = options.imei;
            BaseCollection.prototype.fetch.apply(this, arguments);
        }
    });

    return RecommendCollection;
});

