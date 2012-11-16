/*jslint browser: true, devel: true, indent: 4, nomen:true, vars: true */
/*global define */

define(function (require, exports, module) {
    "use strict";

    var $ = require('../../lib/jquery');
    var Backbone = require('../../lib/backbone');
    var BaseView = require('../BaseView');

    var HomePage = Backbone.View.extend({
        initialize: function () {
            BaseView.prototype.initialize.apply(this, arguments);

            var RecomendForm = require('../form/RecomendForm');
            this.recomendForm = new RecomendForm();
            this.recomendForm.on('submit', this.onRecSubmit.bind(this));
            this.recomendForm.$('input.nick-name').focus();

            var RecomendCollection = require('../../collection/RecomendCollection');
            this.recomendCollection = new RecomendCollection();
        },

        
        /* -------------------- Event Listener ----------------------- */
        
        onRecSubmit: function (imei) {
            this.recomendCollection.on('success', function (recomends) {
                this.off('success');
                console.log('recomends = ' + recomends);
            });
            this.recomendCollection.fetch({
                imei: imei
            });
        }
    });
    
    return HomePage;
});
