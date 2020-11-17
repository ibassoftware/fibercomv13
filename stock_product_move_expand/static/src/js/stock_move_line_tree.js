odoo.define('stock_product_move_expand.stock.move.line.tree', function (require) {
"use strict";
    var core = require('web.core');
    var ListController = require('web.ListController');
    var ListView = require('web.ListView');
    var viewRegistry = require('web.view_registry');

    var QWeb = core.qweb;

    var StockMoveLineListController = ListController.extend({
        /**
         * Extends the renderButtons function of ListView by adding a button
         * on the payslip list.
         *
         * @override
         */
        renderButtons: function () {
            const self = this;
            this._super.apply(this, arguments);
            this.$buttons.append($(QWeb.render("StockListView.expand_moves", this)));
            this.$buttons.on('click', '.btn_expand_moves', function () {
                Object.values(self.model.localData).forEach((val) => {
                    val.openGroupByDefault = true;
                    val.isOpen = true;
                });
                self.reload();
            });
        }
    });

    var StockMoveLineListView = ListView.extend({
        config: _.extend({}, ListView.prototype.config, {
            Controller: StockMoveLineListController,
        }),
    });

    viewRegistry.add('stock_move_line_tree', StockMoveLineListView);
});
