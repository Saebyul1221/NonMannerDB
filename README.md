# 우마공 비매너 DB 라이브러리

> `pip install NonMannerDB`

**사용 예시**

> ```py
> import NonMannerDB
> import asyncio
>
>
> async main():
>   client = NonMannerDB.NonManner()
>   result = client.search_by_name("Username")
>
>   print(result) # {'success': True, 'value': {'count': 0, 'list': []}}
>
> asyncio.run(main())
> ```

**사용 가능한 메서드 종류**

- **`search_by_name(username="유저 이름", skip=0, limit=100)`**
- **`get_all(skip=0, limit=100)`**
- **`get_count(uuid="유저 UUID")`**
- **`get_user(uuid="유저 UUID")`**  
  skip, limit 파라미터는 생략할 수 있습니다.
