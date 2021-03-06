# Generated by Django 2.0.2 on 2018-03-11 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_auto_20180310_2108'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.CharField(blank=True, default='', max_length=5, null=True, verbose_name='得分')),
                ('text', models.TextField(blank=True, default='', null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '答案',
                'verbose_name_plural': '答案',
            },
        ),
        migrations.CreateModel(
            name='AnswerSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='提交时间')),
                ('is_active', models.BooleanField(default=True)),
                ('total_score', models.CharField(default='-1', max_length=5, verbose_name='总得分')),
            ],
            options={
                'verbose_name': '答卷',
                'verbose_name_plural': '答卷',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='AssessmentRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='提交时间')),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='judge', to=settings.AUTH_USER_MODEL, verbose_name='评分人')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to=settings.AUTH_USER_MODEL, verbose_name='受评人')),
            ],
            options={
                'verbose_name': '考勤关系',
                'verbose_name_plural': '考勤关系',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(max_length=20, verbose_name='评价指标')),
                ('question_content', models.CharField(max_length=200, verbose_name='评价要素')),
                ('full_score', models.IntegerField(verbose_name='标准分值')),
                ('order_in_list', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '问题',
                'verbose_name_plural': '问题',
            },
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('type', models.CharField(choices=[('down2up', '下对上'), ('up2down', '上对下'), ('up2up', '平级')], default='up2up', max_length=20, verbose_name='类型')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Department', verbose_name='所属部门')),
                ('question', models.ManyToManyField(related_name='questionnaire_level_question', to='performance.Question', verbose_name='问题')),
            ],
            options={
                'verbose_name': '问卷',
                'verbose_name_plural': '问卷',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='assessmentrelationship',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performance.Questionnaire', verbose_name='对应问卷'),
        ),
        migrations.AddField(
            model_name='answersheet',
            name='answer_sheet_base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performance.AssessmentRelationship', verbose_name='对应问卷'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performance.AnswerSheet', verbose_name='对应答卷'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performance.Question', verbose_name='对应问题'),
        ),
    ]
