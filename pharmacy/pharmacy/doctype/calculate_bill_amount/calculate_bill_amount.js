// Copyright (c) 2020, crio and contributors
// For license information, please see license.txt

frappe.ui.form.on('Calculate Bill Amount', {
	// refresh: function(frm) {

	// }

	get_bills:function(frm){
		frappe.call({
			method: "pharmacy.pharmacy.doctype.calculate_bill_amount.calculate_bill_amount.get_bills",
			freeze: true,
            args: {doc:frm.doc},
            callback: function(r) {
				if(r.message){
					var total_amount = 0;
                    cur_frm.clear_table('bill_list');
                    r.message.forEach(function(element) {
						var c = frm.add_child("bill_list");
						c.bill_no = element.name;
						c.bill_date = element.bill_date;
						c.bill_amount = element.amount;
						c.bill_status = element.bill_status;

						total_amount = total_amount + element.amount;
					});
					refresh_field("bill_list");
                    frm.set_value('total_amount',total_amount);
				}
				frm.refresh_field('total_amount');
                frm.save();
			}
        })}
		
});
