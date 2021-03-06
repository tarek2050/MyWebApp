# Generated by Django 3.0.5 on 2020-06-18 19:44

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('beatStoreApp', '0021_auto_20200618_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Category',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('drumKit', 'Drum Kit'), ('midiKit', 'Midi Kit'), ('samplePack', 'Loop Kit'), ('preset', 'Preset'), ('dawPlugin', 'Daw & Plugin'), ('tutorial', 'Tutorial')], max_length=52, null=True),
        ),
    ]
