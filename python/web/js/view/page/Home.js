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

            var RecommendCollection = require('../../collection/RecommendCollection');
            this.recommendCollection = new RecommendCollection();

            var InstallCollection = require('../../collection/InstallCollection');
            this.installCollection = new InstallCollection();
        },
        
        renderRecommendList: function (recommends) {
            if (!this.recommendList) {
                var RecommendList = require('../list/RecommendList');
                this.recommendList = new RecommendList();
                this.$('.recommend-list-wrap').append(this.recommendList.el);
            }
            this.recommendList.render(recommends);
        },
        
        renderInstallList: function (installs) {
            if (!this.installList) {
                var InstallList = require('../list/InstallList');
                this.installList = new InstallList();
                this.$('.install-list-wrap').append(this.installList.el);
            }
            this.installList.render(installs);
        },

        /* -------------------- Event Listener ----------------------- */
        
        onRecSubmit: function (imei) {
            this.recommendCollection.on('success', function (recommends) {
                this.recommendCollection.off('success');
                this.renderRecommendList(recommends);
            }, this);
            this.recommendCollection.fetch({
                imei: imei
            });

            this.installCollection.on('success', function (installs) {
                this.installCollection.off('success');
                this.renderInstallList(installs);
            }, this);
            this.installCollection.fetch({
                imei: imei
            });
        }
    });
    
    return HomePage;
});
