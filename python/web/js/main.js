/*jslint browser: true, devel: true, indent: 4, nomen:true, vars: true */
/*global define */

define(function (require, exports, module) {
    "use strict";

    var Backbone = require('./lib/backbone');
    var $ = require('./lib/jquery');

    var page = $('#pageName').val();

    var mod = './view/page/' + page;
    require.async(mod, function (Page) {
        var page = new Page();
    });
});

