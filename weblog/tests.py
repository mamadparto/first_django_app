from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import Posts


class WeblogPostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="user1")
        cls.post1 = Posts.objects.create(
            title="post1",
            text="hello this is test post",
            status="pub",
            author=user
        )

        cls.post2 = Posts.objects.create(
            title="post2",
            text="lorem ipsum hello world",
            status=Posts.STATUS_CHOICES[1][0],
            author=user
        )

    def test_post_name_title(self):
        self.assertEquals(str(self.post2), self.post2.title)

    def test_url_post_list(self):
        response = self.client.get("/weblog/")
        self.assertEquals(response.status_code, 200)

    def test_post_url_name(self):
        response = self.client.get(reverse("list_of_post"))
        self.assertEquals(response.status_code, 200)

    def test_post_title_on_weblog_list_page(self):
        response = self.client.get(reverse("list_of_post"))
        self.assertContains(response, self.post1.title)

    def test_detail_post_url(self):
        response = self.client.get(f"/weblog/{self.post1.id}")
        self.assertEquals(response.status_code, 200)

    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse("post_detail", args=[self.post2.id]))
        self.assertEquals(response.status_code, 200)

    def test_post_name_title_on_weblog_detail_page(self):
        response = self.client.get(reverse("post_detail", args=[self.post2.id]))
        self.assertContains(response, self.post2.title)
        self.assertContains(response, self.post2.text)

    def test_post_details_on_weblog_detail_page(self):
        response = self.client.get(f'/weblog/{self.post1.id}')
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_published_or_draft_contains_in_weblog(self):
        response = self.client.get(reverse("list_of_post"))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_status_404_post_is_not_exist(self):
        response = self.client.get(reverse("post_detail", args=[999]))
        self.assertEquals(response.status_code, 404)

    def test_post_create_view(self):
        response = self.client.post(reverse("create_post"), {
            "title": "title1",
            "text": "this is text of title1",
            "status": "pub",
            "author": self.post2.author.id,
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Posts.objects.last().title, "title1")
        self.assertEquals(Posts.objects.last().text, "this is text of title1")

    def test_post_update_view(self):
        response = self.client.post(reverse("update_post", args=[self.post2.id]), {
            "title": "post update1",
            "text": "this text is update1",
            "status": "pub",
            "author": self.post2.author.id,
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Posts.objects.last().title, "post update1")
        self.assertEquals(Posts.objects.last().text, "this text is update1")

    def test_post_delete_view(self):
        response = self.client.post(reverse("delete_post", args=[self.post2.id]))
        self.assertEquals(response.status_code, 302)
