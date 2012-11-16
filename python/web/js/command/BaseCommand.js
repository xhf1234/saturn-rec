/*jslint browser: true, devel: true, indent: 4, nomen:true, vars: true */
/*global define */

define(function (require, exports, module) {
    "use strict";

    var Backbone = require('../lib/backbone');
    var $ = require('../lib/jquery');
    var _ = require('../lib/underscore');

    var BaseCommand = Backbone.Event.extend({
        execute: function () {
            this.options = this.options || {};
            var request = $.ajax(_.extend({
                url: this.url,
                method: this.method
            }, this.obtions));
            request.done(this.success);
        },
        
        success: function (response) {
            //abstract method
        }
        
    });

    return BaseCommand;
    
});

