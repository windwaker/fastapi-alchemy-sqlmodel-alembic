# FastAPI + SQLModel + Alembic

https://testdriven.io/blog/fastapi-sqlmodel/

https://github.com/testdrivenio/fastapi-sqlmodel-alembic

Tasks:

1. Rework song endpoints to abstract out crud functions
2. Inject special test DB with seeded data for tests
   1. https://fastapi.tiangolo.com/advanced/testing-database/
3. Inject real app for integration version of tests to ensure we don't maintain two suites of tests
4. Rework Song endpoints to work for players
5. Split APIs into separate routes & files
