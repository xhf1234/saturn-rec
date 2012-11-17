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
            },

            error: function (jqXHR, textStatus, errorThrown) {
                console.log('textStatus = ' + textStatus);
            }
        },

        fetch: function (options) {
            options = options || {};
            _.defaults(options, this.fetchOptions);
            options.success = options.success.bind(this);
            options.error = options.error.bind(this);
            Backbone.Collection.prototype.fetch.call(this, options);
        },
        
        onFetchSuccess: function (datas) {
            this.trigger('success', datas);
        }
        
    });

    return BaseCollection;
});

