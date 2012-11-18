/*jslint browser: true, devel: true, indent: 4, nomen:true, vars: true */
/*global define */

define(function (require, exports, module) {
    "use strict";

    var Backbone = require('../../lib/backbone');
    var BaseForm = require('./BaseForm');

    var Form = BaseForm.extend({

        events: {
            'click .btn-submit': 'onSubmit',
            'click .random-imei': 'onSelectUser'
        },

        initialize: function () {
            var form = this;
            this.$('.user-imei').keyup(function (e) {
                if (e.which === 13) {
                    form.onSubmit(e);
                }
            });
        },

        
        /* -------------------- Event Listener ----------------------- */
        
        onSelectUser: function (evt) {
            evt.preventDefault();
            this.$('.user-imei').val(evt.currentTarget.text);
            this.onSubmit(evt);
        },

        onSubmit: function (evt) {
            evt.preventDefault();
            var imei = this.$('.user-imei').val();
            if (!imei) {
                alert('请输入用户标识');
            } else {
                this.trigger('submit', imei);
            }
        }
    });

    return Form;
});
