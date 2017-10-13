package dao;

import api.ReceiptResponse;
import generated.tables.records.ReceiptsRecord;
import generated.tables.records.TagsRecord;
import org.jooq.Configuration;
import org.jooq.DSLContext;
import org.jooq.impl.DSL;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

import static com.google.common.base.Preconditions.checkState;
import static generated.Tables.RECEIPTS;
import static generated.Tables.TAGS;

public class TagsDao {
    DSLContext dsl;

    public TagsDao(Configuration jooqConfig) {
        this.dsl = DSL.using(jooqConfig);
    }

    public int insert(String tagName, Integer receipt_id) {

        List<TagsRecord> tagsRecordList = dsl
                .selectFrom(TAGS)
                .where(TAGS.TAG.eq(tagName).and(TAGS.RECEIPT_ID.eq(receipt_id))).fetch();

        if (tagsRecordList != null && tagsRecordList.size() > 0) {
            for (TagsRecord record : tagsRecordList) {
                dsl.deleteFrom(TAGS)
                        .where(TAGS.ID.eq(record.getId()))
                        .execute();

                // return after just one iteration
                return -1;
            }
        } else {
            TagsRecord tagsRecord = dsl
                    .insertInto(TAGS, TAGS.TAG, TAGS.RECEIPT_ID)
                    .values(tagName, receipt_id)
                    .returning(TAGS.ID)
                    .fetchOne();

            checkState(tagsRecord != null && tagsRecord.getId() != null, "Insert failed");

            return tagsRecord.getId();
        }

        return 0;
    }

    public List<ReceiptsRecord> getTaggedReceipts(String tagName) {


        List<TagsRecord> tagsRecordList = dsl
                .selectFrom(TAGS)
                .where(TAGS.TAG.eq(tagName)).fetch();

        if (tagsRecordList == null || tagsRecordList.size() < 1) {
            return new ArrayList<>();

        } else {

            List<ReceiptsRecord> receiptsRecordList = new ArrayList<>();
            for (TagsRecord record : tagsRecordList) {

                receiptsRecordList.addAll(dsl.selectFrom(RECEIPTS)
                        .where(RECEIPTS.ID.eq(record.getReceiptId())).fetch());
            }

            return receiptsRecordList;
        }
    }
}
