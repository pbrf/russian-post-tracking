import russian_post_tracking.soap from RussianPostTracking

barcode = 'bardcode'
login = 'login'
password = 'password'

tracking = RussianPostTracking(barcode, login, password)
history = tracking.get_history()
history = tracking.get_order_events()
