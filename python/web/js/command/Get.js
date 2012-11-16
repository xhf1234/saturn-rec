/*jslint browser: true, devel: true, indent: 4, nomen:true, vars: true */
/*global define */

define(function (require, exports, module) {
    "use strict";

    var BaseCommand = require('./BaseCommand');

    var Get = BaseCommand.extend({
        method: 'GET'
    });

    return Get;
});

