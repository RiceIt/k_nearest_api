##Deployment
2. **pip install requriments.txt**
3. **create postgreSQL database**
4. **set environment variables:**
+ POSTGRESQL_USER
+ POSTGRESQL_PASSWORD 
+ POSTGRESQL_SERVER 
+ DB_NAME
5. **alembic upgrade head**
6. **uvicorn main:app --reload**

##API
#### GET
+ /user/{user_id}
+ /k_nearest/?user_id=user_id&k=k&radius=radius

#### POST
+ /user/  
> {  
> id:	int,  
> name: string,  
> coord: string  
> }  
