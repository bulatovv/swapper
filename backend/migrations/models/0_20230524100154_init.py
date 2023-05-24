from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "trade" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "email" VARCHAR(320) NOT NULL UNIQUE,
    "verified_at" TIMESTAMP,
    "password_hash" VARCHAR(72) NOT NULL,
    "name" TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS "idx_user_email_1b4f1c" ON "user" ("email");
CREATE TABLE IF NOT EXISTS "authtoken" (
    "token" VARCHAR(64) NOT NULL  PRIMARY KEY,
    "user_id" INT NOT NULL UNIQUE REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "item" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "title" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "image_url" TEXT NOT NULL,
    "owner_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "registrationconfirm" (
    "token" VARCHAR(64) NOT NULL  PRIMARY KEY,
    "user_id" INT NOT NULL UNIQUE REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);
CREATE TABLE IF NOT EXISTS "item_trade" (
    "trade_id" INT NOT NULL REFERENCES "trade" ("id") ON DELETE CASCADE,
    "item_id" INT NOT NULL REFERENCES "item" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "user_trade" (
    "trade_id" INT NOT NULL REFERENCES "trade" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
