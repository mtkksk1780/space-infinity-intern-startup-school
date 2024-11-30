/*
  Warnings:

  - Added the required column `submissionStatus` to the `Submission` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "Submission" ADD COLUMN     "submissionStatus" TEXT NOT NULL,
ALTER COLUMN "progressRate" DROP NOT NULL,
ALTER COLUMN "progressComment" DROP NOT NULL;
