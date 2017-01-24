=======
Install
=======

.. code-block:: bash

    pip install russian-post-tracking

=======
Example
=======

.. code-block:: python

    from russian_post_tracking.soap import RussianPostTracking

    barcode = 'bardcode'

    login = 'login'

    password = 'password'

    tracking = RussianPostTracking(barcode, login, password)

    history = tracking.get_history()

    history = tracking.get_order_events()

=======
License
=======

MIT
