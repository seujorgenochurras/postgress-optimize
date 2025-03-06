-- CreateIndex
CREATE INDEX "Card_active_userId_idx" ON "Card"("active", "userId");

-- CreateIndex
CREATE INDEX "Task_cardId_status_idx" ON "Task"("cardId", "status");
