DROP DATABASE IF EXISTS threads;

CREATE DATABASE IF NOT EXISTS threads DEFAULT CHARSET utf8;

USE threads;

CREATE TABLE IF NOT EXISTS thread (
  `id` INT AUTO_INCREMENT COMMENT 'id',
  `thread_id` VARCHAR(100) NOT NULL COMMENT 'thread id',
  `sender_id` VARCHAR(255) NOT NULL COMMENT 'sender id',
  `receiver_id` VARCHAR(255) NOT NULL COMMENT 'receiver id',
  `message_id` INT NOT NULL COMMENT 'message id',
  `is_read` TINYINT DEFAULT 0 COMMENT 'has read or not',
  `created_at` INT UNSIGNED NOT NULL COMMENT 'created at',
  `updated_at` INT UNSIGNED NOT NULL COMMENT 'updated at',
  PRIMARY KEY (`id`),
  KEY `idx_thread_id` (`thread_id`),
  KEY `idx_sender_id` (`sender_id`),
  KEY `idx_receiver_id` (`receiver_id`)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS message (
  `id` INT UNSIGNED AUTO_INCREMENT COMMENT 'id',
  `thread_id` VARCHAR(100) NOT NULL COMMENT 'thread id',
  `sender_id` VARCHAR(255) NOT NULL COMMENT 'sender id',
  `receiver_id` VARCHAR(255) NOT NULL COMMENT 'receiver id',
  `content` VARCHAR(400) NOT NULL COMMENT 'content',
  `created_at` INT UNSIGNED NOT NULL COMMENT 'created at',
  PRIMARY KEY (`id`),
  KEY `idx_thread_id` (`thread_id`),
  KEY `idx_sender_id` (`sender_id`),
  KEY `idx_receiver_id` (`receiver_id`)
)ENGINE=InnoDB;