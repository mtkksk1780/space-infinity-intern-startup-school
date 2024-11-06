-- AlterTable
ALTER TABLE "Submission" ALTER COLUMN "outputUrl" DROP NOT NULL;

-- AlterTable
ALTER TABLE "User" ALTER COLUMN "password" DROP NOT NULL,
ALTER COLUMN "name" DROP NOT NULL;
