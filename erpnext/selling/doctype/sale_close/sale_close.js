//Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
//For license information, please see license.txt

frappe.ui.form
		.on(
				'Sale Close',
				{
					refresh : function(frm) {

						var today = frm.doc.date;

						var Current_User = user;
						frappe
								.call({
									"method" : "erpnext.selling.doctype.sale_close.sale_close.day_close",
									args : {
										doctype : "Sale Close",
										"user" : user,
										"today" : today,

									},
									callback : function(data) {

										frm.doc.cash_mode = data.message[0]['Cash'];
										cur_frm.refresh_field("cash_mode");

										frm.doc.card_mode = data.message[0]['Credit Card'];
										cur_frm.refresh_field("card_mode");

										total = (frm.doc.cash_mode)
												+ (frm.doc.card_mode);
										frm.doc.total_system_sales = total;
										cur_frm
												.refresh_field("total_system_sales");
										// alert(data.message[0]['Credit
										// Card']);
										// alert(data.message[0]['Cash']);
									}
								})

					},

					data_10 : function(frm) {
						var label_two_thousand = frm.doc.label_two_thousand;

						var data_10 = frm.doc.data_10;
						var two_thous = label_two_thousand * data_10;
						frm.doc.two_thousand = two_thous;
						cur_frm.refresh_field("two_thousand");
						total_cash_cal(frm);

					},
					data_14 : function(frm) {
						var label_five_hundred = frm.doc.label_five_hundred;
						var data_14 = frm.doc.data_14;
						var five_hundred = label_five_hundred * data_14;
						frm.doc.five_hundred = five_hundred;
						cur_frm.refresh_field("five_hundred");
						total_cash_cal(frm);
					},

					data_18 : function(frm) {
						var label_two_hundred = frm.doc.label_two_hundred;
						var data_18 = frm.doc.data_18;
						var two_hundred = label_two_hundred * data_18;
						frm.doc.two_hundred = two_hundred;
						cur_frm.refresh_field("two_hundred");
						total_cash_cal(frm);

					},
					data_188 : function(frm) {
						var label_one_hundred = frm.doc.label_one_hundred;
						var data_188 = frm.doc.data_188;
						var one_hundred = label_one_hundred * data_188;
						frm.doc.one_hundred = one_hundred;
						cur_frm.refresh_field("one_hundred");
						total_cash_cal(frm);

					},
					data_199 : function(frm) {
						var label_fifty = frm.doc.label_fifty;
						var data_199 = frm.doc.data_199;
						var fifty = label_fifty * data_199;
						frm.doc.fifty = fifty;
						cur_frm.refresh_field("fifty");
						total_cash_cal(frm);

					},
					data_200 : function(frm) {
						var label_twenty = frm.doc.label_twenty;
						var data_200 = frm.doc.data_200;
						var twenty = label_twenty * data_200;
						frm.doc.twenty = twenty;
						cur_frm.refresh_field("twenty");
						total_cash_cal(frm);

					},
					data_201 : function(frm) {
						var label_ten = frm.doc.label_ten;
						var data_201 = frm.doc.data_201;
						var ten = label_ten * data_201;
						frm.doc.ten = ten;
						cur_frm.refresh_field("ten");
						total_cash_cal(frm);

					},
					data_210 : function(frm) {
						var label_coin = frm.doc.label_coin;
						var data_210 = frm.doc.data_210;
						var coin = label_coin * data_210;
						frm.doc.coin = coin;
						cur_frm.refresh_field("coin");
						total_cash_cal(frm);

					},

				});

function total_cash_cal(frm) {
	
	var two_thousand = frm.doc.two_thousand;
	var five_hundred = frm.doc.five_hundred;
	var two_hundred = frm.doc.two_hundred;
	var one_hundred = frm.doc.one_hundred;
	var fifty = frm.doc.fifty;
	var twenty = frm.doc.twenty;
	var ten = frm.doc.ten;
	var coin = frm.doc.coin;

	total = parseInt(two_thousand) + parseInt(five_hundred)
			+ parseInt(two_hundred) + parseInt(one_hundred) + parseInt(fifty)
			+ parseInt(twenty) + parseInt(ten) + parseInt(coin);

	frm.doc.total_cash = total;
	cur_frm.refresh_field("total_cash");
	
	var cash_mode=frm.doc.cash_mode
	var total_cash = frm.doc.total_cash;
	
	if(cash_mode>total_cash)
		{
	var cash_difference_pass = parseInt(cash_mode) - parseInt(total_cash);
	frm.doc.cash_difference = (cash_difference_pass)*(-1);
	cur_frm.refresh_field("cash_difference");
	
		}
	if(cash_mode<=total_cash)
	{
		var cash_difference_pass = parseInt(cash_mode) - parseInt(total_cash);
		frm.doc.cash_difference = (cash_difference_pass)*(-1);
		cur_frm.refresh_field("cash_difference");

	}

	
	
	
}
