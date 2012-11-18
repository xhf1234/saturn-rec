/*jslint browser: true, devel: true, indent: 4, nomen:true, vars: true */
/*global define */

define(function (require, exports, module) {
    "use strict";

    var $ = require('../../lib/jquery');
    var BasePage = require('./BasePage');

    var HomePage = BasePage.extend({

        initialize: function () {
            BasePage.prototype.initialize.apply(this, arguments);

            var RecommendForm = require('../form/RecommendForm');
            this.recommendForm = new RecommendForm({
                el: '.form-rec'
            });
            this.recommendForm.on('submit', this.onRecSubmit.bind(this));
            this.recommendForm.$('input.nick-name').focus();
        },
        
        /* -------------------- Event Listener ----------------------- */
        
        onRecSubmit: function (imei) {
            var options = {imei: imei};

            if (!this.recommendList) {
                var RecommendList = require('../list/RecommendList');
                this.recommendList = new RecommendList();
                this.$('.recommend-list-wrap').append(this.recommendList.el);
            }
            this.recommendList.fetch(options);

            if (!this.installList) {
                var InstallList = require('../list/InstallList');
                this.installList = new InstallList();
                this.$('.install-list-wrap').append(this.installList.el);
            }
            this.installList.fetch(options);
        }
    });
    
    return HomePage;
});
