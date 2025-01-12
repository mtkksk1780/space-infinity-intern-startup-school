/*
  Warnings:

  - Added the required column `isActiveWeek` to the `Submission` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "Submission" ADD COLUMN     "isActiveWeek" BOOLEAN NOT NULL;
