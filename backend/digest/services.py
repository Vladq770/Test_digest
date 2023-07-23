from django.db.models import Count, F
from datetime import datetime, timedelta
from core.models import User, Blog, Post, Tag, Subscription, Like, Comment
from .models import Digest
from core.serializers import PostSerializer
from .serializers import DigestSerializer
from .schemas import DigestParams


def create_digest_service(params):
    digest_params = DigestParams(**params)
    user = User.objects.get(pk=digest_params.id)
    digest = Digest.objects.create(user=user)
    blogs = Subscription.objects.filter(user=user).values('blog')
    date = datetime.now() - timedelta(days=3)
    posts = Post.objects.filter(blog__in=blogs, created_at__gte=date).annotate(ordering=F('views') + F('likes') * 2 + Count('comment') * 3)\
        .order_by('-ordering', '-created_at')[digest_params.offset : digest_params.offset + digest_params.limit]
    digest.posts.add(*posts)
    res = PostSerializer(posts, many=True).data
    return res, 200
