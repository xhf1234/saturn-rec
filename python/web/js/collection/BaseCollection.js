/*jslint browser: true, devel: true, indent: 4, nomen:true, vars: true */
/*global define */

define(function (require, exports, module) {
    "use strict";

    var Backbone = require('../lib/backbone');
    var _ = require('../lib/underscore');

    var BaseCollection = Backbone.Collection.extend({

        fetchOptions: {
            success: function () {
                this.onFetchSuccess(this.toJSON());
            }
        },

        initialize: function () {
            Backbone.Collection.prototype.initialize.apply(this, arguments);

            this.fetchOptions.success.bind(this);
        },

        fetch: function (options) {
            options = options || {};
            _.defaults(options, this.fetchOptions);
            Backbone.Collection.prototype.fetch.apply(this, options);
        },
        
        onFetchSuccess: function (datas) {
            this.trigger('success', datas);
        }
        
    });

    return BaseCollection;
});

