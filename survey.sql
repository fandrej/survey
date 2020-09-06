/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES  */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Дамп структуры для таблица main.poll_poll
CREATE TABLE IF NOT EXISTS "poll_poll" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "date_start" datetime NOT NULL,
    "date_end" datetime NULL,
    "note" text NULL,
    "name" varchar(100) NOT NULL
);

-- Дамп данных таблицы main.poll_poll: -1 rows
/*!40000 ALTER TABLE "poll_poll" DISABLE KEYS */;
INSERT INTO "poll_poll" ("id", "date_start", "date_end", "note", "name") VALUES
	(1, '2020-05-13 14:01:35.645994', '2020-05-31 14:01:18', 'описание', 'Тест 1'),
	(21, '2020-05-14 21:01:15.008586', '2020-05-31 14:01:18', 'описание', 'Тест 2'),
	(22, '2020-05-14 21:04:21.579374', '2020-05-31 14:01:18', 'описание', 'Тест 2'),
	(23, '2020-05-17 20:07:41.275786', '2020-05-31 14:01:18', 'описание', 'Тест 3'),
	(26, '2020-05-17 21:22:06.129612', '2020-05-31 14:01:18', 'описание', 'Тест 1'),
	(27, '2020-05-17 21:23:16.782030', '2020-05-31 14:01:18', 'описание', 'Тест 1'),
	(28, '2020-05-17 21:25:42.994819', '2020-05-31 14:01:18', 'описание', 'Тест 1'),
	(29, '2020-05-17 21:27:16.438968', '2020-05-31 14:01:18', 'описание', 'Тест 1'),
	(30, '2020-05-17 21:34:15.897010', '2020-05-31 14:01:18', 'описание', 'Тест 1'),
	(31, '2020-05-17 21:41:25.993166', '2020-05-31 14:01:18', 'описание', 'Тест 1'),
	(32, '2020-05-17 21:42:29.681422', '2020-05-31 14:01:18', 'описание', 'Тест 1'),
	(33, '2020-05-17 21:50:21.208631', '2020-05-31 14:01:18', 'описание', 'Тест 1'),
	(34, '2020-05-17 21:56:58.572889', '2020-05-31 14:01:18', 'описание', 'Тест 1'),
	(35, '2020-05-17 22:02:31.945671', '2020-05-31 14:01:18', 'описание', 'Тест 1'),
	(36, '2020-05-17 22:03:30.141268', '2020-05-31 14:01:18', 'описание', 'Тест 1'),
	(37, '2020-05-17 22:03:56.477795', '2020-05-31 14:01:18', 'описание', 'Тест 1'),
	(38, '2020-05-17 22:05:37.242421', '2020-05-31 14:01:18', 'описание', 'Тест 1'),
	(39, '2020-05-17 22:06:54.454970', '2020-05-31 14:01:18', 'описание', 'Тест 1'),
	(40, '2020-05-17 22:07:06.168619', '2020-05-31 14:01:18', 'описание', 'Тест 1'),
	(41, '2020-05-17 22:11:27.894870', '2020-05-31 14:01:18', 'описание', 'Тест 1'),
	(42, '2020-05-17 22:38:26.579042', '2020-05-31 14:01:18', 'описание', 'Тест 1'),
	(43, '2020-05-17 22:39:24.373151', '2020-05-31 14:01:18', 'описание', 'Тест 1');
/*!40000 ALTER TABLE "poll_poll" ENABLE KEYS */;

-- Дамп структуры для таблица main.poll_questions
CREATE TABLE IF NOT EXISTS "poll_questions" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "question_type" varchar(10) NOT NULL,
    "poll_id" integer NOT NULL REFERENCES "poll_poll" ("id") DEFERRABLE INITIALLY DEFERRED,
    "question_text" varchar(100) NOT NULL,
    "question_options" varchar(100) NULL
);

-- Дамп данных таблицы main.poll_questions: -1 rows
/*!40000 ALTER TABLE "poll_questions" DISABLE KEYS */;
INSERT INTO "poll_questions" ("id", "question_type", "poll_id", "question_text", "question_options") VALUES
	(0, 'variants', 23, 'Когда рак на горе ...?', 'Прыгент, Сдохнет, Свистнет'),
	(2, 'text', 1, 'Имя', ''),
	(3, 'variant', 1, '2 * 2 =', '3,4,5'),
	(20, 'variants', 1, 'Как?', 'Быстро, Дёшево, Качественно'),
	(33, 'text', 21, 'Имя', ''),
	(34, 'text', 21, 'Фамилия', ''),
	(35, 'text', 22, 'Имя', ''),
	(36, 'text', 22, 'Фамилия', ''),
	(44, 'variants', 1, 'Когда рак на горе ...?', 'Прыгент, Сдохнет, Свистнет'),
	(45, 'text', 23, 'Имя', ''),
	(46, 'text', 23, 'Фамилия', ''),
	(47, 'text', 23, 'Имя', ''),
	(52, 'variants', 23, 'Когда рак на горе ...?', 'Прыгент, Сдохнет, Свистнет'),
	(53, 'text', 23, 'sdfsdf', ''),
	(54, 'text', 28, 'Имя', ''),
	(55, 'text', 28, 'Фамилия', ''),
	(56, 'text', 38, 'Имя', ''),
	(57, 'text', 38, 'Фамилия', ''),
	(58, 'text', 39, 'Имя', ''),
	(59, 'text', 39, 'Фамилия', ''),
	(60, 'text', 40, 'Имя', ''),
	(61, 'text', 40, 'Фамилия', ''),
	(62, 'text', 41, 'Имя', ''),
	(63, 'text', 41, 'Фамилия', ''),
	(64, 'text', 23, 'sdfsdf', ''),
	(65, 'text', 23, 'aaaaaaaaaaaaaaaa', ''),
	(66, 'text', 43, 'Имя', ''),
	(67, 'text', 43, 'Фамилия', '');
/*!40000 ALTER TABLE "poll_questions" ENABLE KEYS */;

-- Дамп структуры для таблица main.poll_vote
CREATE TABLE IF NOT EXISTS "poll_vote" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "poll_id" integer NOT NULL REFERENCES "poll_poll" ("id") DEFERRABLE INITIALLY DEFERRED,
    "question_id" integer NOT NULL REFERENCES "poll_questions" ("id") DEFERRABLE INITIALLY DEFERRED,
    "answer" text NOT NULL,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
);

-- Дамп данных таблицы main.poll_vote: -1 rows
/*!40000 ALTER TABLE "poll_vote" DISABLE KEYS */;
INSERT INTO "poll_vote" ("id", "poll_id", "question_id", "answer", "user_id") VALUES
	(1, 1, 2, 'aaa', 1),
	(2, 1, 3, '3', 1),
	(3, 1, 20, 'Быстро, Дёшево', 1),
	(4, 21, 33, 'aaaaaaaaa', 1),
	(5, 21, 34, 'bbbbbbbb', 1),
	(6, 1, 2, 'test', 2),
	(7, 1, 3, '1', 2),
	(8, 1, 20, 'Дёшево, Качественно', 2),
	(9, 21, 33, 'test', 2),
	(10, 21, 34, 'test test', 2);
/*!40000 ALTER TABLE "poll_vote" ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
