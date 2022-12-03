from flask import Flask, render_template, request, redirect

from models.city import City
import repositories.city_repository as city_repository