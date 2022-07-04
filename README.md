# vk_expert_api
____
**vk_experts_api** – Python модуль для автоматизации деятельности в программе [Эксперты ВКонтакте](https://vk.com/vkexperts)

Токен следует использовать от VK ME: 
https://oauth.vk.com/token?grant_type=password&client_id=6146827&client_secret=qVxWRF1CwHERuIrKBnqe&username=логин&password=пароль&v=5.131&2fa_supported=1

[Неофициальная документация](https://www.notion.so/VK-API-Experts-3a12796f3bdf45c4bf500d5005c32a78)

```python
import vk_experts_api

# Авторизация
vk = vk_experts_api.Expert(
    token="abcd", category=5)

# Получение поста
post = vk.getCustom(count=1, start_from=2)

# Выставление оценки
vk.setPostVote(post_id=post["items"][0]["post_id"],
               owner_id=post["items"][0]["post_id"],
               new_vote=-1)
```

