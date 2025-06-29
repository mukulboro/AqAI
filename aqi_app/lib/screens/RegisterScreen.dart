import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import "package:aqi_app/constants/urls.dart" as urls;

class RegisterScreen extends StatefulWidget {
  const RegisterScreen({super.key});

  @override
  State<RegisterScreen> createState() => _RegisterScreenState();
}

class _RegisterScreenState extends State<RegisterScreen> {
  final _formKey = GlobalKey<FormState>();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  final _firstNameConrtoller = TextEditingController();
  final _middleNameController = TextEditingController();
  final _lastNameController = TextEditingController();
  final _confirmPasswordController = TextEditingController();
  final emailRegex = RegExp(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$');

  Future<void> _submitForm({
    required firstName,
    required midName,
    required lastName,
    required email,
    required pass,
  }) async {
    final apiUri = Uri.parse(urls.kREGISTER_MANUAL_URL);
    try {
      final response = await http.post(
        apiUri,
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          "first_name": firstName,
          "middle_name": midName,
          "last_name": lastName,
          "email": email,
          "password": pass,
        }),
      );
      if (response.statusCode == 200 || response.statusCode == 201) {
        // Success response
        print('Registration successful');
      } else {
        // Some error
        print('Failed: ${response.body}');
      }
    } catch (e) {
      print("Error: ${e}");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Register Page"), backgroundColor: Colors.red),
      body: Center(
        child: Form(
          key: _formKey,
          child: ListView(
            children: [
              Column(
                children: [
                  TextFormField(
                    controller: _firstNameConrtoller,
                    decoration: InputDecoration(labelText: "First Name"),
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please enter first name';
                      }
                      return null;
                    },
                  ),
                  TextFormField(
                    controller: _middleNameController,
                    decoration: InputDecoration(labelText: "Middle Name"),
                  ),
                  TextFormField(
                    controller: _lastNameController,
                    decoration: InputDecoration(labelText: "Last Name"),
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please enter last name';
                      }
                      return null;
                    },
                  ),
                  TextFormField(
                    controller: _emailController,
                    decoration: InputDecoration(labelText: "Email"),
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please enter the email';
                      }
                      if (!emailRegex.hasMatch(value)) {
                        return 'Please enter a valid email address';
                      }
                      return null;
                    },
                  ),
                  TextFormField(
                    controller: _passwordController,
                    obscureText: true,
                    decoration: InputDecoration(labelText: "Password"),
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please enter the password';
                      }
                      if (value.length < 8) {
                        return '8 vanda chhoto vo';
                      }
                      return null;
                    },
                  ),
                  TextFormField(
                    controller: _confirmPasswordController,
                    obscureText: true,
                    decoration: InputDecoration(labelText: "Confirm Password"),
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please enter the password';
                      }
                      if (value != _passwordController.text) {
                        return "Passwords Do Not Match";
                      }
                      return null;
                    },
                  ),
                  MaterialButton(
                    onPressed: () async {
                      if (_formKey.currentState!.validate()) {
                        await _submitForm(
                          firstName: _firstNameConrtoller.text,
                          midName: _middleNameController.text,
                          lastName: _lastNameController.text,
                          email: _emailController.text,
                          pass: _confirmPasswordController.text,
                        );
                      }
                    },
                    child: Text("Register"),
                  ),
                  SizedBox(height: 30),
                  ElevatedButton(
                    onPressed: () {},
                    child: Text("Register with Google"),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
