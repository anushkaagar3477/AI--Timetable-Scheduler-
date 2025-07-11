from django.db import migrations, models
from django.db.models import deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_number',
                 models.CharField(max_length=5,
                                  primary_key=True,
                                  serialize=False)),
                ('course_name', models.CharField(max_length=40)),
                ('max_numb_students', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('dept_name', models.CharField(max_length=50)),
                ('courses', models.ManyToManyField(to='SchedulerApp.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('uid', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingTime',
            fields=[
                ('pid',
                 models.CharField(max_length=4,
                                  primary_key=True,
                                  serialize=False)),
                ('time',
                 models.CharField(choices=[('9:30 - 10:30', '9:30 - 10:30'),
                                           ('10:30 - 11:30', '10:30 - 11:30'),
                                           ('11:30 - 12:30', '11:30 - 12:30'),
                                           ('12:30 - 1:30', '12:30 - 1:30'),
                                           ('2:30 - 3:30', '2:30 - 3:30'),
                                           ('3:30 - 4:30', '3:30 - 4:30'),
                                           ('4:30 - 5:30', '4:30 - 5:30')],
                                  default='11:30 - 12:30',
                                  max_length=50)),
                ('day',
                 models.CharField(choices=[('Monday', 'Monday'),
                                           ('Tuesday', 'Tuesday'),
                                           ('Wednesday', 'Wednesday'),
                                           ('Thursday', 'Thursday'),
                                           ('Friday', 'Friday'),
                                           ('Saturday', 'Saturday')],
                                  max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('r_number', models.CharField(max_length=6)),
                ('seating_capacity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('section_id',
                 models.CharField(max_length=25,
                                  primary_key=True,
                                  serialize=False)),
                ('course',
                 models.ForeignKey(blank=True,
                                   null=True,
                                   on_delete=deletion.CASCADE,
                                   to='SchedulerApp.Course')),
                ('department',
                 models.ForeignKey(on_delete=deletion.CASCADE,
                                   to='SchedulerApp.Department')),
                ('instructor',
                 models.ForeignKey(blank=True,
                                   null=True,
                                   on_delete=deletion.CASCADE,
                                   to='SchedulerApp.Instructor')),
                ('meeting_time',
                 models.ForeignKey(blank=True,
                                   null=True,
                                   on_delete=deletion.CASCADE,
                                   to='SchedulerApp.MeetingTime')),
                ('room',
                 models.ForeignKey(blank=True,
                                   null=True,
                                   on_delete=deletion.CASCADE,
                                   to='SchedulerApp.Room')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(to='SchedulerApp.Instructor'),
        ),
    ]
