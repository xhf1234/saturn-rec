/*jslint browser: true, devel: true, indent: 4, nomen:true, vars: true */
/*global define */

define(function (require, exports, module) {
    "use strict";

    var $ = require('jquery');
    var RecomendForm = require('../view/RecomendForm');
    var recomendForm = new RecomendForm();

    recomendForm.$('input.nick-name').focus();
});
