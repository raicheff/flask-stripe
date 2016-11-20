#
# Flask-Stripe
#
# Copyright (C) 2014 Boris Raicheff
# All rights reserved
#


from flask.signals import Namespace


namespace = Namespace()


#: Occurs whenever an account status or property has changed.
#: describes an account
account_updated = namespace.signal('account.updated')

#: Occurs whenever a user deauthorizes an application. Sent to the related
#: application only.
#: describes an application
account_application_deauthorized = namespace.signal('account.application.deauthorized')

#: Occurs whenever an external account is created.
#: describes an external account
account_external_account_created = namespace.signal('account.external_account.created')

#: Occurs whenever an external account is deleted.
#: describes an external account
account_external_account_deleted = namespace.signal('account.external_account.deleted')

#: Occurs whenever an external account is updated.
#: describes an external account
account_external_account_updated = namespace.signal('account.external_account.updated')

#: Occurs whenever an application fee is created on a charge.
#: describes an application fee
application_fee_created = namespace.signal('application_fee.created')

#: Occurs whenever an application fee is refunded, whether from refunding a
#: charge or from refunding the application fee directly, including partial
#: refunds.
#: describes an application fee
application_fee_refunded = namespace.signal('application_fee.refunded')

#: Occurs whenever an application fee refund is updated.
#: describes a fee refund
application_fee_refund_updated = namespace.signal('application_fee.refund.updated')

#: Occurs whenever your Stripe balance has been updated (e.g. when a charge
#: collected is available to be paid out). By default, Stripe will automatically
#: transfer any funds in your balance to your bank account on a daily basis.
#: describes a balance
balance_available = namespace.signal('balance.available')

#: Occurs whenever a receiver has been created.
#: describes a bitcoin receiver
bitcoin_receiver_created = namespace.signal('bitcoin.receiver.created')

#: Occurs whenever a receiver is filled (that is, when it has received enough
#: bitcoin to process a payment of the same amount).
#: describes a bitcoin receiver
bitcoin_receiver_filled = namespace.signal('bitcoin.receiver.filled')

#: Occurs whenever a receiver is updated.
#: describes a bitcoin receiver
bitcoin_receiver_updated = namespace.signal('bitcoin.receiver.updated')

#: Occurs whenever bitcoin is pushed to a receiver.
#: describes a bitcoin receiver
bitcoin_receiver_transaction_created = namespace.signal('bitcoin.receiver.transaction.created')

#: Occurs whenever a previously uncaptured charge is captured.
#: describes a charge
charge_captured = namespace.signal('charge.captured')

#: Occurs whenever a failed charge attempt occurs.
#: describes a charge
charge_failed = namespace.signal('charge.failed')

#: Occurs whenever a charge is refunded, including partial refunds.
#: describes a charge
charge_refunded = namespace.signal('charge.refunded')

#: Occurs whenever a new charge is created and is successful.
#: describes a charge
charge_succeeded = namespace.signal('charge.succeeded')

#: Occurs whenever a charge description or metadata is updated.
#: describes a charge
charge_updated = namespace.signal('charge.updated')

#: Occurs when the dispute is resolved and the dispute status changes to won or
#: lost.
#: describes a dispute
charge_dispute_closed = namespace.signal('charge.dispute.closed')

#: Occurs whenever a customer disputes a charge with their bank (chargeback).
#: describes a dispute
charge_dispute_created = namespace.signal('charge.dispute.created')

#: Occurs when funds are reinstated to your account after a dispute is won.
#: describes a dispute
charge_dispute_funds_reinstated = namespace.signal('charge.dispute.funds_reinstated')

#: Occurs when funds are removed from your account due to a dispute.
#: describes a dispute
charge_dispute_funds_withdrawn = namespace.signal('charge.dispute.funds_withdrawn')

#: Occurs when the dispute is updated (usually with evidence).
#: describes a dispute
charge_dispute_updated = namespace.signal('charge.dispute.updated')

#: Occurs whenever a coupon is created.
#: describes a coupon
coupon_created = namespace.signal('coupon.created')

#: Occurs whenever a coupon is deleted.
#: describes a coupon
coupon_deleted = namespace.signal('coupon.deleted')

#: Occurs whenever a coupon is updated.
#: describes a coupon
coupon_updated = namespace.signal('coupon.updated')

#: Occurs whenever a new customer is created.
#: describes a customer
customer_created = namespace.signal('customer.created')

#: Occurs whenever a customer is deleted.
#: describes a customer
customer_deleted = namespace.signal('customer.deleted')

#: Occurs whenever any property of a customer changes.
#: describes a customer
customer_updated = namespace.signal('customer.updated')

#: Occurs whenever a coupon is attached to a customer.
#: describes a discount
customer_discount_created = namespace.signal('customer.discount.created')

#: Occurs whenever a customer's discount is removed.
#: describes a discount
customer_discount_deleted = namespace.signal('customer.discount.deleted')

#: Occurs whenever a customer is switched from one coupon to another.
#: describes a discount
customer_discount_updated = namespace.signal('customer.discount.updated')

#: Occurs whenever a new source is created for the customer.
#: describes a source (e.g., card or Bitcoin receiver)
customer_source_created = namespace.signal('customer.source.created')

#: Occurs whenever a source is removed from a customer.
#: describes a source (e.g., card or Bitcoin receiver)
customer_source_deleted = namespace.signal('customer.source.deleted')

#: Occurs whenever a source's details are changed.
#: describes a source (e.g., card or Bitcoin receiver)
customer_source_updated = namespace.signal('customer.source.updated')

#: Occurs whenever a customer with no subscription is signed up for a plan.
#: describes a subscription
customer_subscription_created = namespace.signal('customer.subscription.created')

#: Occurs whenever a customer ends their subscription.
#: describes a subscription
customer_subscription_deleted = namespace.signal('customer.subscription.deleted')

#: Occurs three days before the trial period of a subscription is scheduled to
#: end.
#: describes a subscription
customer_subscription_trial_will_end = namespace.signal('customer.subscription.trial_will_end')

#: Occurs whenever a subscription changes. Examples would include switching from
#: one plan to another, or switching status from trial to active.
#: describes a subscription
customer_subscription_updated = namespace.signal('customer.subscription.updated')

#: Occurs whenever a new invoice is created. If you are using webhooks, Stripe
#: will wait one hour after they have all succeeded to attempt to pay the
#: invoice; the only exception here is on the first invoice, which gets created
#: and paid immediately when you subscribe a customer to a plan. If your
#: webhooks do not all respond successfully, Stripe will continue retrying the
#: webhooks every hour and will not attempt to pay the invoice. After 3 days,
#: Stripe will attempt to pay the invoice regardless of whether or not your
#: webhooks have succeeded. See how to respond to a webhook.
#: describes an invoice
invoice_created = namespace.signal('invoice.created')

#: Occurs whenever an invoice attempts to be paid, and the payment fails. This
#: can occur either due to a declined payment, or because the customer has no
#: active card. A particular case of note is that if a customer with no active
#: card reaches the end of its free trial, an invoice.payment_failed
#: notification will occur.
#: describes an invoice
invoice_payment_failed = namespace.signal('invoice.payment_failed')

#: Occurs whenever an invoice attempts to be paid, and the payment succeeds.
#: describes an invoice
invoice_payment_succeeded = namespace.signal('invoice.payment_succeeded')

#: Occurs whenever an invoice changes (for example, the amount could change).
#: describes an invoice
invoice_updated = namespace.signal('invoice.updated')

#: Occurs whenever an invoice item is created.
#: describes an invoiceitem
invoiceitem_created = namespace.signal('invoiceitem.created')

#: Occurs whenever an invoice item is deleted.
#: describes an invoiceitem
invoiceitem_deleted = namespace.signal('invoiceitem.deleted')

#: Occurs whenever an invoice item is updated.
#: describes an invoiceitem
invoiceitem_updated = namespace.signal('invoiceitem.updated')

#: Occurs whenever an order is created.
#: describes an order
order_created = namespace.signal('order.created')

#: Occurs whenever payment is attempted on an order, and the payment fails.
#: describes an order
order_payment_failed = namespace.signal('order.payment_failed')

#: Occurs whenever payment is attempted on an order, and the payment succeeds.
#: describes an order
order_payment_succeeded = namespace.signal('order.payment_succeeded')

#: Occurs whenever an order is updated.
#: describes an order
order_updated = namespace.signal('order.updated')

#: Occurs whenever a plan is created.
#: describes a plan
plan_created = namespace.signal('plan.created')

#: Occurs whenever a plan is deleted.
#: describes a plan
plan_deleted = namespace.signal('plan.deleted')

#: Occurs whenever a plan is updated.
#: describes a plan
plan_updated = namespace.signal('plan.updated')

#: Occurs whenever a product is created.
#: describes a product
product_created = namespace.signal('product.created')

#: Occurs whenever a product is updated.
#: describes a product
product_updated = namespace.signal('product.updated')

#: Occurs whenever a recipient is created.
#: describes a recipient
recipient_created = namespace.signal('recipient.created')

#: Occurs whenever a recipient is deleted.
#: describes a recipient
recipient_deleted = namespace.signal('recipient.deleted')

#: Occurs whenever a recipient is updated.
#: describes a recipient
recipient_updated = namespace.signal('recipient.updated')

#: Occurs whenever a SKU is created.
#: describes a sku
sku_created = namespace.signal('sku.created')

#: Occurs whenever a SKU is updated.
#: describes a sku
sku_updated = namespace.signal('sku.updated')

#: Occurs whenever a new transfer is created.
#: describes a transfer
transfer_created = namespace.signal('transfer.created')

#: Occurs whenever Stripe attempts to send a transfer and that transfer fails.
#: describes a transfer
transfer_failed = namespace.signal('transfer.failed')

#: Occurs whenever a sent transfer is expected to be available in the
#: destination bank account. If the transfer failed, a transfer.failed webhook
#: will additionally be sent at a later time.
#: Note to Connect users: this event is only created for transfers from your
#: connected Stripe accounts to their bank accounts, not for transfers to the
#: connected accounts themselves.
#: describes a transfer
transfer_paid = namespace.signal('transfer.paid')

#: Occurs whenever a transfer is reversed, including partial reversals.
#: describes a transfer
transfer_reversed = namespace.signal('transfer.reversed')

#: Occurs whenever the description or metadata of a transfer is updated.
#: describes a transfer
transfer_updated = namespace.signal('transfer.updated')

#: May be sent by Stripe at any time to see if a provided webhook URL is
#: working.
#: has no description
ping = namespace.signal('ping')


# EOF
