/*
  Warnings:

  - You are about to drop the column `register_date` on the `Project` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE "Project" DROP COLUMN "register_date",
ADD COLUMN     "registerDate" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
