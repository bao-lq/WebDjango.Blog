from django.test import TestCase
from .models import Post

# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        Post.objects.create(
            title = 'myTitle',
            body = 'test case',
        )

    def test_string_representation(self):
        post = Post(title ='my entry Title')
        self.assertEqual(str(post), str('id: ' + str(post.id) + ' title: ' + post.title + '\n'))

    def test_post_list_view(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'myTitle')
        self.assertTemplateUsed(response, 'blogs/blog.html', 'pages/base.html')

    def test_post_detail_view(self):
        response = self.client.get('/blog/1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'myTitle')
        self.assertTemplateUsed(response, 'blogs/post.html', 'pages/base.html')