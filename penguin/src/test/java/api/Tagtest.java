package api;
import generated.tables.records.TagsRecord;
import io.dropwizard.jersey.validation.Validators;
import org.junit.Test;

import javax.validation.Validator;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.collection.IsEmptyCollection.empty;

public class Tagtest {
    private final Validator validator = Validators.newValidator();

    @Test
    public void TagTest() {
        TagsRecord tagsRecord = new TagsRecord();
        tagsRecord.setTag("dummy");
        tagsRecord.setReceiptId(1);

        validator.validate(tagsRecord);
        assertThat(validator.validate(tagsRecord), empty());
    }

}