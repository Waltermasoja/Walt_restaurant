from django.test import TestCase
from django.utils import timezone
from .models import post
from datetime import timedelta
from django.utils import reverse

class postmodeltest(TestCase):
    def test_was_published_recently_with_future_dates(self):
        time = timezone.now() + timedelta(days=30)
        future_post = post(date_published = time)
        self.assertIs(future_post.recently_published(),False)

    def test_was_published_recently_with_recent_post(self):
        """
        Should return false if the question was published more than one day ago
        """   
        time = timezone.now() - timedelta(days=1,seconds=1)
        old_post = post(date_published = time)
        self.assertIs(old_post.recently_published(),False)