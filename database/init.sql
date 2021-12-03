DROP TABLE IF EXISTS "guess";
DROP TABLE IF EXISTS "question";
DROP TABLE IF EXISTS "person_episode";
DROP TABLE IF EXISTS "episode";
DROP TABLE IF EXISTS "cos_character";
DROP TABLE IF EXISTS "person";

CREATE TABLE "episode" (
  "id" INTEGER NOT NULL,
  "yt_id" TEXT NOT NULL ,
  "title" TEXT NOT NULL,
  "thumbnail" TEXT,
  "duration" REAL,
  "view_count" INTEGER,
  "like_count" INTEGER,
  "comment_count" INTEGER,
  "description" TEXT,
  "date" datetime NULL,
  "created" timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY ("id" AUTOINCREMENT),
  UNIQUE("yt_id") ON CONFLICT IGNORE
);

CREATE TABLE "person" (
  "id" INTEGER NOT NULL,
  "handle" TEXT NULL,
  "name" TEXT NULL,
  "created" timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY ("id" AUTOINCREMENT),
  UNIQUE("handle", "name") ON CONFLICT IGNORE
);

CREATE TABLE "person_episode" (
  "id" INTEGER NOT NULL,
  "person_id" INTEGER NOT NULL,
  "episode_id" INTEGER NOT NULL,
  "created" timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY ("id" AUTOINCREMENT),
  FOREIGN KEY("person_id") REFERENCES person("id"),
  FOREIGN KEY("episode_id") REFERENCES episode("id"),
  UNIQUE("person_id", "episode_id") ON CONFLICT IGNORE
);


CREATE TABLE "cos_character" (
  "id" INTEGER NOT NULL,
  "name" TEXT NOT NULL,
  "series" TEXT NULL,
  "created" timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY ("id" AUTOINCREMENT)
);

CREATE TABLE "question" (
  "id" INTEGER NOT NULL,
  "episode_id" INTEGER NOT NULL,
  "cluegiver_person_id" INTEGER NOT NULL,
  "answer_character_id" INTEGER NOT NULL,
  "clue1" TEXT,
  "clue2" TEXT,
  "clue3" TEXT,
  "clue4" TEXT,
  "clue5" TEXT,
  "created" timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY ("id" AUTOINCREMENT),
  FOREIGN KEY ("episode_id") REFERENCES episode("id"),
  FOREIGN KEY ("cluegiver_person_id") REFERENCES person("id"),
  FOREIGN KEY ("answer_character_id") REFERENCES cos_character("id")
);

CREATE TABLE "guess" (
  "id" INTEGER NOT NULL,
  "question_id" INTEGER NOT NULL,
  "guesser_person_id" INTEGER NOT NULL,
  "character_id" INTEGER NOT NULL,
  "clue_number" INTEGER NOT NULL,
  "created" timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY ("id" AUTOINCREMENT),
  FOREIGN KEY ("question_id") REFERENCES question("id"),
  FOREIGN KEY ("guesser_person_id") REFERENCES person("id"),
  FOREIGN KEY ("character_id") REFERENCES cos_character("id")
);