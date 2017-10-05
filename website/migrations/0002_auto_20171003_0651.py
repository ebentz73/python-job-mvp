# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-03 06:51
from __future__ import unicode_literals

from django.db import migrations, models
import website.profile


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='founder',
            name='employee_count',
            field=models.IntegerField(verbose_name='Employees'),
        ),
        migrations.AlterField(
            model_name='founder',
            name='field',
            field=models.CharField(choices=[('EDUC', 'Education'), ('TECH', 'Technology'), ('RE', 'Retail'), ('HEAL', 'Health Care'), ('ECOM', 'E-Commerce'), ('MARK', 'Marketplaces'), ('FIN', 'Finance'), ('HARD', 'Hardware'), ('MANG', 'Management/Consulting'), ('LEG', 'Legal'), ('MED', 'Medical'), ('HOUS', 'Real Estate'), ('AUTO', 'Automotive'), ('ENER', 'Energy'), ('MACH', 'Machinery'), ('ENV', 'Environmental'), ('NONE', 'Other')], max_length=4, verbose_name='Field'),
        ),
        migrations.AlterField(
            model_name='founder',
            name='logo',
            field=website.profile.CustomImageField(upload_to=website.profile.company_logo_path),
        ),
        migrations.AlterField(
            model_name='founder',
            name='stage',
            field=models.CharField(choices=[('0', 'Idea'), ('1', 'Prototype'), ('2', 'Incorporated'), ('3', 'Generating Revenue'), ('4', 'Seed'), ('5', 'Series A'), ('6', 'Series B'), ('7', 'Series C')], max_length=1, verbose_name='Stage'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hours_week',
            field=models.CharField(blank=True, choices=[('0', '0 - 5'), ('1', '5 - 10'), ('2', '10 - 15'), ('3', '15 - 20'), ('4', '20+')], max_length=1, verbose_name='Hours per Week'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=website.profile.CustomImageField(upload_to=website.profile.user_directory_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='major',
            field=models.CharField(blank=True, choices=[('EECS', 'Electrical Engineering and Computer Science'), ('IEOR', 'Industrial Engineering and Operations Research'), ('ECON', 'Economics'), ('AMATH', 'Applied Math'), ('CHEM', 'Chemistry'), ('PHYS', 'Physics'), ('MECH', 'Mechanical Engineering'), ('BIOE', 'Bioengineering'), ('CS', 'Computer Science'), ('STAT', 'Statistics'), ('HAAS', 'Business'), ('PH', 'Public Health'), ('MCB', 'MCB'), ('BIO', 'Biology'), ('UND', 'Undecided'), ('NONE', 'Other')], max_length=5, verbose_name='Major'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='positions',
            field=website.profile.ChoiceArrayField(base_field=models.CharField(choices=[('0', 'Partnership'), ('1', 'Intern'), ('2', 'Part-Time'), ('3', 'Full-Time'), ('4', 'Contract')], default='0', max_length=1), size=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('MARK', 'Marketing'), ('BIZ', 'Business/Administration'), ('SALE', 'Sales'), ('DES', 'Design'), ('PM', 'Product Manager'), ('CS', 'Software engineer'), ('HARD', 'Hardware engineer'), ('IOS', 'Mobile developer'), ('CONS', 'Consulting'), ('HR', 'Human resources'), ('NONE', 'Other')], max_length=4),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate'), ('PH', 'PhD'), ('PD', 'Post-Doc'), ('AL', 'Alumni'), ('FC', 'Faculty'), ('NONE', 'Other')], max_length=4, verbose_name='Cal Association'),
        ),
    ]
